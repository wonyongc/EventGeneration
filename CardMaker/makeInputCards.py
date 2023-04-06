import os
pjoin=os.path.join


flavor= "ele" #options are: ele/mu/tau
sigmodel = 'doublet' #options are: singlet/doublet


#Initialize
if(sigmodel == 'doublet'):
    model = 'VLLD'
    inputdir='skeleton/doublet'
else:
    model = 'VLLS'
    inputdir='skeleton/singlet'

##skeleton cards
extramodel_card = f"{model}_{flavor}_M100_extramodels.dat"
customize_card  = f"{model}_{flavor}_M100_customizecards.dat"
proc_card       = f"{model}_{flavor}_M100_proc_card.dat"
run_card        = f"{model}_{flavor}_M100_run_card.dat"

#######################################################

#VLLMass=[100,125,150,200,250,300,350,400,500,600,700,800] #for singlet
VLLMass=[100,200] #for doublet

for mass in VLLMass:
    card_dir=f"{model}_{flavor}_M{mass}"
    os.system(f"mkdir {card_dir}")
    
    #copy skeleton cards
    os.system(f"cp {inputdir}/{extramodel_card} {card_dir}/")
    os.system(f"cp {inputdir}/{customize_card} {card_dir}/")
    os.system(f"cp {inputdir}/{proc_card} {card_dir}/")
    os.system(f"cp {inputdir}/{run_card} {card_dir}/")

    #change name according to mass
    cardlist = os.listdir(card_dir)
    for f in cardlist:
        tag=f.split(f'{model}_{flavor}_M100_')[1]

        newname = f"{model}_{flavor}_M{mass}_{tag}"

        os.system(f"mv {card_dir}/{f} {card_dir}/{newname}")

    ##show on terminal
    print(f"\nInput cards in {card_dir} after renaming...")
    print(os.listdir(card_dir))


    ## change content using sed

    customize_card_sed = f"sed -i 's/100/{mass}/g' {card_dir}/{model}_{flavor}_M{mass}_customizecards.dat"
    os.system(customize_card_sed)

    proc_card_sed = f"sed -i 's/100/{mass}/g' {card_dir}/{model}_{flavor}_M{mass}_proc_card.dat"
    os.system(proc_card_sed)