SetContext Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Diagnostics Namespace](topic1498.md) > [IRuleAnalyzerService Interface](topic1500.md) : SetContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    Object that contains rule to analyze

_specificationProject_
    The owning project for the context.

Glossary Item Box

Sets the object will that be shown in the rule analyzer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetContext( _
       ByVal _context_ As [IHasRule](topic5947.md), _
       ByVal _specificationProject_ As [Project](topic3859.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IRuleAnalyzerService](topic1500.md)
    Dim context As [IHasRule](topic5947.md)
    Dim specificationProject As [Project](topic3859.md)
     
    instance.SetContext(context, specificationProject)  
  
C#|   
---|---  
      
    
    void SetContext( 
       [IHasRule](topic5947.md) _context_ ,
       [Project](topic3859.md) _specificationProject_
    )  
  
#### Parameters

 _context_
    Object that contains rule to analyze
 _specificationProject_
    The owning project for the context.

# Remarks

This will update the analyze button's enabled state depending on a valid context.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IRuleAnalyzerService Interface](topic1500.md)   
[IRuleAnalyzerService Members](topic1501.md)


