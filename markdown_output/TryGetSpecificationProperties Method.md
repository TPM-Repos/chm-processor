![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetSpecificationProperties Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3405.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : TryGetSpecificationProperties Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationDetails_
    The details of the specification to retrieve properties for.

_specificationProperties_
    The properties for this specification.

Glossary Item Box

Tries to get all of the specification properties for the given specification. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetSpecificationProperties( _
       ByVal _specificationDetails_ As [SpecificationDetails](topic11292.md), _
       ByRef _specificationProperties_ As IDictionary(Of String,String) _
    ) As [SpecificationPropertiesResult](topic2363.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationDetails As [SpecificationDetails](topic11292.md)
    Dim specificationProperties As IDictionary(Of String,String)
    Dim value As [SpecificationPropertiesResult](topic2363.md)
     
    value = instance.TryGetSpecificationProperties(specificationDetails, specificationProperties)  
  
C#|   
---|---  
      
    
    public [SpecificationPropertiesResult](topic2363.md) TryGetSpecificationProperties( 
       [SpecificationDetails](topic11292.md) _specificationDetails_ ,
       ref IDictionary<string,string> _specificationProperties_
    )  
  
#### Parameters

 _specificationDetails_
    The details of the specification to retrieve properties for.
_specificationProperties_
    The properties for this specification.

#### Return Value

An enum that represents whether the properties were retrieved successfully. If not, the enum will give the reason for the failure.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
