![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGenerator Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13677.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FormatGeneratorFactory Class](topic13670.md) : GetGenerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_extension_
    The file extension to get the generator for e.g. ".pdf"

Glossary Item Box

Gets a generator from the specified file extension. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetGenerator( _
       ByVal _extension_ As String _
    ) As [FileFormatGenerator](topic13579.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FormatGeneratorFactory](topic13670.md)
    Dim extension As String
    Dim value As [FileFormatGenerator](topic13579.md)
     
    value = instance.GetGenerator(extension)  
  
C#|   
---|---  
      
    
    public [FileFormatGenerator](topic13579.md) GetGenerator( 
       string _extension_
    )  
  
#### Parameters

 _extension_
    The file extension to get the generator for e.g. ".pdf"

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FormatGeneratorFactory Class](topic13670.md)   
[FormatGeneratorFactory Members](topic13671.md)

©2024 DriveWorks Ltd. All Rights Reserved.
