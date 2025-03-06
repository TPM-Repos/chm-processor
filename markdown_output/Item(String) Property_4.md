![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14902.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFeatureCollection Class](topic14887.md) > [Item Property](topic14900.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the feature to retrieve.

Glossary Item Box

Gets the feature with the specified address 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _address_ As String _
    ) As [ReleasedFeature](topic14875.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFeatureCollection](topic14887.md)
    Dim address As String
    Dim value As [ReleasedFeature](topic14875.md)
     
    value = instance.Item(address)  
  
C#|   
---|---  
      
    
    public [ReleasedFeature](topic14875.md) Item( 
       string _address_
    ) {get;}  
  
#### Parameters

 _address_
    The address of the feature to retrieve.

# ![](dotnetimages/collapse.gif)Remarks

This property performs a linear search of the features, looking for one with the specified address, and thus has O(N) worst case running time.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedFeatureCollection Class](topic14887.md)   
[ReleasedFeatureCollection Members](topic14888.md)   
[Overload List](topic14900.md)

©2024 DriveWorks Ltd. All Rights Reserved.
