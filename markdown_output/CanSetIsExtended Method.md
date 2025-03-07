Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanSetIsExtended Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : CanSetIsExtended Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control to check.

Glossary Item Box

Determines whether the property can be extended. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CanSetIsExtended( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.CanSetIsExtended(control)  
  
C#|   
---|---  
      
    
    public bool CanSetIsExtended( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control to check.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


