Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFeatureCollection Class](topic14887.md) : Add Method  
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

_suppressionStateValue_
    The value of the suppression state of the feature.

Glossary Item Box

Adds and returns a new feature. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _address_ As String, _
       ByVal _featureType_ As String, _
       ByVal _suppressionStateValue_ As String _
    ) As [ReleasedFeature](topic14875.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFeatureCollection](topic14887.md)
    Dim name As String
    Dim address As String
    Dim featureType As String
    Dim suppressionStateValue As String
    Dim value As [ReleasedFeature](topic14875.md)
     
    value = instance.Add(name, address, featureType, suppressionStateValue)  
  
C#|   
---|---  
      
    
    public [ReleasedFeature](topic14875.md) Add( 
       string _name_ ,
       string _address_ ,
       string _featureType_ ,
       string _suppressionStateValue_
    )  
  
#### Parameters

 _name_
    The DriveWorks name of the feature.
_address_
    The SolidWorks address of the feature.
_featureType_
    The specific type of the feature, or an empty string if the feature is captured as a generic feature.
_suppressionStateValue_
    The value of the suppression state of the feature.

#### Return Value

The newly added feature.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFeatureCollection Class](topic14887.md)   
[ReleasedFeatureCollection Members](topic14888.md)


