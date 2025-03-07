Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Evaluate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks.StandardConditions Namespace](topic6735.md) > [CheckValueComponentTaskReleaseCondition Class](topic6737.md) : Evaluate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationContext_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function Evaluate( _
       ByVal _specificationContext_ As [SpecificationContext](topic11149.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CheckValueComponentTaskReleaseCondition](topic6737.md)
    Dim specificationContext As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.Evaluate(specificationContext)  
  
C#|   
---|---  
      
    
    protected override bool Evaluate( 
       [SpecificationContext](topic11149.md) _specificationContext_
    )  
  
#### Parameters

 _specificationContext_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CheckValueComponentTaskReleaseCondition Class](topic6737.md)   
[CheckValueComponentTaskReleaseCondition Members](topic6738.md)


