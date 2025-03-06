TryGetSpecificationProperties Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetSpecificationProperties( _
       ByVal _specificationDetails_ As [SpecificationDetails](topic11292.md), _
       ByRef _specificationProperties_ As IDictionary(Of String,String) _
    ) As [SpecificationPropertiesResult](topic2363.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


