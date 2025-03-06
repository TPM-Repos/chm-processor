SetInputValue(Object,InputValueType) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) > [SetInputValue Method](topic7720.md) : SetInputValue(Object,InputValueType) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to set to the input property.

_type_
    The type of the input value.

Glossary Item Box

Sets the current input value of the control, if it has one. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Overloads Overridable Sub SetInputValue( _
       ByVal _value_ As Object, _
       ByVal _type_ As [InputValueType](topic7309.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim value As Object
    Dim type As [InputValueType](topic7309.md)
     
    instance.SetInputValue(value, type)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public virtual void SetInputValue( 
       object _value_ ,
       [InputValueType](topic7309.md) _type_
    )  
  
#### Parameters

 _value_
    The value to set to the input property.
_type_
    The type of the input value.

# Remarks

Control implementers should not override [SetInputValue(Object)](topic7721.md) if they already override this method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)   
[Overload List](topic7720.md)


