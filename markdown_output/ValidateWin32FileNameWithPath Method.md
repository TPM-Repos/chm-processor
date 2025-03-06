![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateWin32FileNameWithPath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13325.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateWin32FileNameWithPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fileNameWithPath_
    The name of the file with its path and extension to validate.

Glossary Item Box

Validates a full file path according to NTFS guidelines. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateWin32FileNameWithPath( _
       ByVal _fileNameWithPath_ As String _
    ) As [ValidatePathResult](topic13194.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim fileNameWithPath As String
    Dim value As [ValidatePathResult](topic13194.md)
     
    value = [ValidationUtility](topic13287.md).ValidateWin32FileNameWithPath(fileNameWithPath)  
  
C#|   
---|---  
      
    
    public static [ValidatePathResult](topic13194.md) ValidateWin32FileNameWithPath( 
       string _fileNameWithPath_
    )  
  
#### Parameters

 _fileNameWithPath_
    The name of the file with its path and extension to validate.

#### Return Value

True if the path validates correctly, and false otherwise.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)

©2024 DriveWorks Ltd. All Rights Reserved.
