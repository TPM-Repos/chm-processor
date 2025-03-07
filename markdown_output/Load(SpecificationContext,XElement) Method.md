Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load(SpecificationContext,XElement) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) > [Load Method](topic6310.md) : Load(SpecificationContext,XElement) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationContext_
    The specification loading the results.

_savedResults_
    The saved release results.

Glossary Item Box

Loads the released component results from the given XML. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Load( _
       ByVal _specificationContext_ As [SpecificationContext](topic11149.md), _
       ByVal _savedResults_ As XElement _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim specificationContext As [SpecificationContext](topic11149.md)
    Dim savedResults As XElement
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = [ReleaseComponentsResults](topic6300.md).Load(specificationContext, savedResults)  
  
C#|   
---|---  
      
    
    public static [ReleaseComponentsResults](topic6300.md) Load( 
       [SpecificationContext](topic11149.md) _specificationContext_ ,
       XElement _savedResults_
    )  
  
#### Parameters

 _specificationContext_
    The specification loading the results.
_savedResults_
    The saved release results.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)   
[Overload List](topic6310.md)


