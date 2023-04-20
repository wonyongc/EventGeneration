import os
pjoin=os.path.join


flavor= "tau" #options are: ele/mu/tau
sigmodel = 'doublet' #options are: singlet/doublet

VLLMass=[1400,1600,1800,2000,2200] #for singlet
#VLLMass=[100] #for doublet



##########################   USER DON'T NEED TO MODIFY AFTER THIS ###################################
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


    #  move the folder in correct place
    #  for singlet: cards/singlet/ele or cards/singlet/mu
    #  for doublet: cards/singlet/ele or cards/singlet/mu
    
    move_cmd= f"mv {card_dir} cards/{sigmodel}/{flavor}/"
    os.system(move_cmd)
    
