SerializeCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : SerializeCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The XML writer to which to write the serialized control data.

_options_
    Options which configure the serialization process.

Glossary Item Box

Serializes the contents of the control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub SerializeCore( _
       ByVal _writer_ As XmlWriter, _
       ByVal _options_ As [SerializationMode](topic7318.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim writer As XmlWriter
    Dim options As [SerializationMode](topic7318.md)
     
    instance.SerializeCore(writer, options)  
  
C#|   
---|---  
      
    
    protected virtual void SerializeCore( 
       XmlWriter _writer_ ,
       [SerializationMode](topic7318.md) _options_
    )  
  
#### Parameters

 _writer_
    The XML writer to which to write the serialized control data.
_options_
    Options which configure the serialization process.

# Remarks

This method is called by the [Serialize](topic7718.md) method after having already written the `<Control Name="$(Name)"> tag.`

After the [SerializeCore](topic7719.md) method has finished executing, the [Serialize](topic7718.md) method will write the ending `</Control>` tag.

By default, this method will serialize all the dynamic properties which have been registered for the control type, and because properties should always come before other content in the control, anyone overriding this method should call [SerializeCore](topic7719.md) before serializing custom content.

To perform custom serialization of a property in a control, specify a custom property converter (see the [DriveWorks.Forms.DataModel.IPropertyValueConverter](topic9373.md) interface documentation for more details) when the property is registered using the [DriveWorks.Forms.DataModel.DynamicProperty.Register](topic9430.md) method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


