![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14207.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _address_ As String, _
       ByVal _featureType_ As String _
    ) As [CapturedFeature](topic14191.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedFeatureCollection Class](topic14201.md)   
[CapturedFeatureCollection Members](topic14202.md)

©2024 DriveWorks Ltd. All Rights Reserved.
