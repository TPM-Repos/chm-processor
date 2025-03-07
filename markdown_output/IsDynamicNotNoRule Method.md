Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDynamicNotNoRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicProperty Class](topic9398.md) : IsDynamicNotNoRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control instance on which to check the property.

Glossary Item Box

Determines whether the property is dynamic, and doesn't have the [PropertyBehavior.FlagNoRuleAllowed](topic9383.md) flag set. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsDynamicNotNoRule( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DynamicProperty](topic9398.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.IsDynamicNotNoRule(control)  
  
C#|   
---|---  
      
    
    public bool IsDynamicNotNoRule( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The control instance on which to check the property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DynamicProperty Members](topic9399.md)


