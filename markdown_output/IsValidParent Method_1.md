Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValidParent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [Form Class](topic8086.md) : IsValidParent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The candidate parent control.

Glossary Item Box

Overridden to prevent parenting the form to any other control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides NotOverridable Function IsValidParent( _
       ByVal _control_ As [ContainerControlBase](topic7684.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Form](topic8086.md)
    Dim control As [ContainerControlBase](topic7684.md)
    Dim value As Boolean
     
    value = instance.IsValidParent(control)  
  
C#|   
---|---  
      
    
    public override bool IsValidParent( 
       [ContainerControlBase](topic7684.md) _control_
    )  
  
#### Parameters

 _control_
    The candidate parent control.

#### Return Value

Overridden to return false in all cases.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Form Class](topic8086.md)   
[Form Members](topic8087.md)


