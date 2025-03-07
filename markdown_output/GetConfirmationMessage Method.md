Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConfirmationMessage Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Task Class](topic11629.md) : GetConfirmationMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

When overridden by a derived class, gets a confirmation message which should be shown to an interactive user before executing the task sequence to which task belongs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function GetConfirmationMessage( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.GetConfirmationMessage(ctx)  
  
C#|   
---|---  
      
    
    protected virtual string GetConfirmationMessage( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

#### Return Value

A confirmation message for the user, or a null reference if no confirmation is necessary.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Class](topic11629.md)   
[Task Members](topic11630.md)


