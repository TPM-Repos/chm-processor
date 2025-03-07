Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NextCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardBase Class](topic1200.md) : NextCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_nextStep_
    The next wizard step.

Glossary Item Box

Attempts navigation to the next wizard step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function NextCore( _
       ByRef _nextStep_ As Control _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WizardBase](topic1200.md)
    Dim nextStep As Control
    Dim value As Boolean
     
    value = instance.NextCore(nextStep)  
  
C#|   
---|---  
      
    
    protected virtual bool NextCore( 
       ref Control _nextStep_
    )  
  
#### Parameters

 _nextStep_
    The next wizard step.

#### Return Value

**true** if navigation succeeds.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WizardBase Class](topic1200.md)   
[WizardBase Members](topic1201.md)


