Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRegisteredToControl Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : IsRegisteredToControl Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control to check

Glossary Item Box

Determines whether the given control has this [DynamicProperty](topic9398.md) registered to it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsRegisteredToControl( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.IsRegisteredToControl(control)  
  
C#|   
---|---  
      
    
    public bool IsRegisteredToControl( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control to check

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


