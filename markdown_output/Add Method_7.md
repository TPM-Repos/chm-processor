Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFeatureCollection Class](topic14201.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The DriveWorks name of the feature.

_address_
    The SolidWorks address of the feature.

_featureType_
    The specific type of the feature, or an empty string if the feature is captured as a generic feature.

Glossary Item Box

Adds and returns a new feature. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _address_ As String, _
       ByVal _featureType_ As String _
    ) As [CapturedFeature](topic14191.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFeatureCollection](topic14201.md)
    Dim name As String
    Dim address As String
    Dim featureType As String
    Dim value As [CapturedFeature](topic14191.md)
     
    value = instance.Add(name, address, featureType)  
  
C#|   
---|---  
      
    
    public [CapturedFeature](topic14191.md) Add( 
       string _name_ ,
       string _address_ ,
       string _featureType_
    )  
  
#### Parameters

 _name_
    The DriveWorks name of the feature.
_address_
    The SolidWorks address of the feature.
_featureType_
    The specific type of the feature, or an empty string if the feature is captured as a generic feature.

#### Return Value

The newly added feature.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFeatureCollection Class](topic14201.md)   
[CapturedFeatureCollection Members](topic14202.md)


