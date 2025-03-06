SetValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : SetValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control on which to set the property.

_value_
    The new value of the property.

Glossary Item Box

Sets the value of the property on the specified control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetValue( _
       ByVal _control_ As [ControlBase](topic7698.md), _
       ByVal _value_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Object
     
    instance.SetValue(control, value)  
  
C#|   
---|---  
      
    
    public void SetValue( 
       [ControlBase](topic7698.md) _control_ ,
       object _value_
    )  
  
#### Parameters

 _control_
    The control on which to set the property.
_value_
    The new value of the property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


