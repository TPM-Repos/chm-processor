Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnActiveDialogOrFormChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : OnActiveDialogOrFormChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data for the event.

Glossary Item Box

Raises the [ActiveDialogOrFormChanged](topic11239.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnActiveDialogOrFormChanged( _
       ByVal _e_ As EventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim e As EventArgs
     
    instance.OnActiveDialogOrFormChanged(e)  
  
C#|   
---|---  
      
    
    protected virtual void OnActiveDialogOrFormChanged( 
       EventArgs _e_
    )  
  
#### Parameters

 _e_
    The event data for the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


