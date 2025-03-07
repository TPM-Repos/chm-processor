Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValidParent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : IsValidParent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The candidate parent control.

Glossary Item Box

Validates whether the control can be added to the specified parent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Overridable Function IsValidParent( _
       ByVal _control_ As [ContainerControlBase](topic7684.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim control As [ContainerControlBase](topic7684.md)
    Dim value As Boolean
     
    value = instance.IsValidParent(control)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public virtual bool IsValidParent( 
       [ContainerControlBase](topic7684.md) _control_
    )  
  
#### Parameters

 _control_
    The candidate parent control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


