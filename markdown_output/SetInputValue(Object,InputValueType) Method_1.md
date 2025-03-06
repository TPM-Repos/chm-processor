       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetInputValue(Object,InputValueType) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [MeasurementTextBox Class](topic8364.md) > [SetInputValue Method](topic8376.md) : SetInputValue(Object,InputValueType) Method  
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
      
    
    Public Overloads Overrides Sub SetInputValue( _
       ByVal _value_ As Object, _
       ByVal _type_ As [InputValueType](topic7309.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [MeasurementTextBox](topic8364.md)
    Dim value As Object
    Dim type As [InputValueType](topic7309.md)
     
    instance.SetInputValue(value, type)  
  
C#|   
---|---  
      
    
    public override void SetInputValue( 
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

[MeasurementTextBox Class](topic8364.md)   
[MeasurementTextBox Members](topic8365.md)   
[Overload List](topic8376.md)


