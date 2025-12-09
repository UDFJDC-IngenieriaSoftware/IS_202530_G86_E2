export interface UserInterface{
    name: string,
    second_name: string,
    first_lastname: string,
    second_lastname: string,
    cedula: string,
    date_of_birth: Date,
    phone: string
}

export interface TreatementInterface{
    cedula: string,
    nombreTratamiento: string,
    especialidad: string,
    fechaInicio: Date,
    fechaFin: Date,
    nombreMedicamento: string,
    dosis: string,
    concentracion: string,
    presentacion: presentacion,
    frecuencia: number,
    reminder: reminderInterface
}

export interface reminderInterface{
    idRecordatorio?: number,
    idTratamiento?: number,
    idMedicamento?: number,
    minutosFaltantes: number,
    notas: string,
    estadoEnvio: EstadoEnvio,
    respuestaPaciente: EstadoRespuesta,
    fechaEnvioRecordatorio: Date,
    fechaRespuesta: Date,
}

export enum EstadoRespuesta{
    Confirmado = "Confirmado",
    SinRespuesta = "Sin respuesta"
}

export enum EstadoEnvio{
    Pendiente = "Pendiente",
    Enviado = "Enviado",
    Error = "Error al enviar"
}

export enum presentacion{
    comprimidos = "comprimidos", 
    cápsulas= "capsulas", 
    jarabes= "jarabes", 
    cremas= "cremas", 
    parches= "parches", 
    inyectables= "inyectables",
    aerosoles= "aerosoles"
}