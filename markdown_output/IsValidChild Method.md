Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValidChild Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ContainerControlBase Class](topic7684.md) : IsValidChild Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The candidate child control.

Glossary Item Box

Validates whether the specified control can be added as a child. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function IsValidChild( _
       ByVal _control_ As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ContainerControlBase](topic7684.md)
    Dim control As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.IsValidChild(control)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public bool IsValidChild( 
       [ControlBase](topic7698.md) _control_
    )  
  
#### Parameters

 _control_
    The candidate child control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ContainerControlBase Class](topic7684.md)   
[ContainerControlBase Members](topic7685.md)


