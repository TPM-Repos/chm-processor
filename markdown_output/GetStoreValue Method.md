Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetStoreValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : GetStoreValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control from which to get the property value.

Glossary Item Box

Gets the current unconverted value of the property from the specified control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetStoreValue( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Object
     
    value = instance.GetStoreValue(control)  
  
C#|   
---|---  
      
    
    public object GetStoreValue( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control from which to get the property value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


