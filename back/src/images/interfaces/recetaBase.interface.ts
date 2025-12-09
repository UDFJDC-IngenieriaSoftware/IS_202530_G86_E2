export interface RecetaInterface{
    paciente:{
        nombre: string,
        identificacion:string 
    },
    medico: {
        nombre: string
    },
    fecha: Date,
    medicamentos: [
        {
        nombre: string,
        dosis: string,
        frecuencia: string,
        duracion: Date
        }
    ],
    notas: string,
}