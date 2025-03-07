Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlDynamicPropertyRule Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlDynamicPropertyRule Class](topic7788.md) : ControlDynamicPropertyRule Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control that the dynamic property belongs to.

_prop_
    The dynamic property.

Glossary Item Box

Creates a new instance of the [ControlDynamicPropertyRule](topic7788.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _control_ As [ControlBase](topic7698.md), _
       ByVal _prop_ As [DynamicProperty](topic9398.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim control As [ControlBase](topic7698.md)
    Dim prop As [DynamicProperty](topic9398.md)
     
    Dim instance As New [ControlDynamicPropertyRule](topic7788.md)(control, prop)  
  
C#|   
---|---  
      
    
    public ControlDynamicPropertyRule( 
       [ControlBase](topic7698.md) _control_ ,
       [DynamicProperty](topic9398.md) _prop_
    )  
  
#### Parameters

 _control_
    The control that the dynamic property belongs to.
_prop_
    The dynamic property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlDynamicPropertyRule Class](topic7788.md)   
[ControlDynamicPropertyRule Members](topic7789.md)


