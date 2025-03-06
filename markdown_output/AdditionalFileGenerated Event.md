![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFileGenerated Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13606.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : AdditionalFileGenerated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an additional file format is saved. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event AdditionalFileGenerated As [FileFormatGenerator.AdditionalFileGeneratedEventHandler](topic13924.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim handler As [FileFormatGenerator.AdditionalFileGeneratedEventHandler](topic13924.md)
     
    AddHandler instance.AdditionalFileGenerated, handler  
  
C#|   
---|---  
      
    
    public event [FileFormatGenerator.AdditionalFileGeneratedEventHandler](topic13924.md) AdditionalFileGenerated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [FileFormatGenerationEventArgs](topic15202.md) containing data related to this event. The following **FileFormatGenerationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[TargetPath](topic15209.md)| Gets the target path.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)

©2024 DriveWorks Ltd. All Rights Reserved.
