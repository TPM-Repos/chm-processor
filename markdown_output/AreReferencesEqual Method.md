![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AreReferencesEqual Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7213.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [LibraryAttribute Class](topic7201.md) : AreReferencesEqual Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reference1_
    The first reference to compare.

_reference2_
    The second reference to compare.

Glossary Item Box

Compares two qualified references for equality. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function AreReferencesEqual( _
       ByVal _reference1_ As String, _
       ByVal _reference2_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim reference1 As String
    Dim reference2 As String
    Dim value As Boolean
     
    value = [LibraryAttribute](topic7201.md).AreReferencesEqual(reference1, reference2)  
  
C#|   
---|---  
      
    
    public static bool AreReferencesEqual( 
       string _reference1_ ,
       string _reference2_
    )  
  
#### Parameters

 _reference1_
    The first reference to compare.
_reference2_
    The second reference to compare.

#### Return Value

True if the references are equivalent, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[LibraryAttribute Class](topic7201.md)   
[LibraryAttribute Members](topic7202.md)

©2024 DriveWorks Ltd. All Rights Reserved.
