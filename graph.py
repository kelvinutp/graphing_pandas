def graficar(data,direccion):
  """
  data= informacion a graficar. Debe estar en pandas.dataframe
  direccion= donde se va a guardar la imagen

  """
  group='Etapa' #column name to groupby
  x_axis='Tiempo(HH:mm:ss)'
  y1=[]
  y2=[]
  y1_label='Voltaje (mV)'
  y2_label='Corriente (mA)'
  
  for b in data.keys():
      if 'Corriente' in b[0]:
          y2.append(b)
      elif 'Voltaje' in b[0]:
          y1.append(b)
  
  #genera grafica por etapa con TODOS los ciclos juntos y la guarda 
  
  x=data.groupby(group)
  for b,c in x:
    c.plot(x=x_axis,
    grid=True,
    figsize=(30,10),
    title=b,
    secondary_y=y2,
    ylabel=y1_label,
    legend=False).right_ax.set_ylabel(y2_label).figure.savefig(os.path.join(direccion+"_"+b+'.jpg'))

 
  return
