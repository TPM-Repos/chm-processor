![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFoldersCreated Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11244.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : AdditionalFoldersCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when additional folders are created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event AdditionalFoldersCreated As [AdditionalFoldersCreatedEventHandler](topic11817.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [AdditionalFoldersCreatedEventHandler](topic11817.md)
     
    AddHandler instance.AdditionalFoldersCreated, handler  
  
C#|   
---|---  
      
    
    public event [AdditionalFoldersCreatedEventHandler](topic11817.md) AdditionalFoldersCreated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [AdditionalFoldersCreatedEventArgs](topic10775.md) containing data related to this event. The following **AdditionalFoldersCreatedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[FullPaths](topic10785.md)| Gets the full paths of the additional folders that were created.   
[RelativePaths](topic10786.md)| Gets the relative paths of the additional folders that were created.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)

©2024 DriveWorks Ltd. All Rights Reserved.
