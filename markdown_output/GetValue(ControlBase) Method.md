Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetValue(ControlBase) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) > [GetValue Method](topic9419.md) : GetValue(ControlBase) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control from which to get the property value.

Glossary Item Box

Gets the current value of the property from the specified control, and converts it to the proper type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetValue( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Object
     
    value = instance.GetValue(control)  
  
C#|   
---|---  
      
    
    public object GetValue( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control from which to get the property value.

#### Return Value

The value of the property, converted using the Converter specified when the property was registered if one was specified.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)   
[Overload List](topic9419.md)


