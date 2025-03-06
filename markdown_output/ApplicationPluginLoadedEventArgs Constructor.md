![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ApplicationPluginLoadedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2122.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ApplicationPluginLoadedEventArgs Class](topic2116.md) : ApplicationPluginLoadedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_applicationPluginInfo_
    Information about the application plugin that was loaded.

Glossary Item Box

Initializes a new instance of the [ApplicationPluginLoadedEventArgs](topic2116.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _applicationPluginInfo_ As [IApplicationPluginInfo](topic2010.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim applicationPluginInfo As [IApplicationPluginInfo](topic2010.md)
     
    Dim instance As New [ApplicationPluginLoadedEventArgs](topic2116.md)(applicationPluginInfo)  
  
C#|   
---|---  
      
    
    public ApplicationPluginLoadedEventArgs( 
       [IApplicationPluginInfo](topic2010.md) _applicationPluginInfo_
    )  
  
#### Parameters

 _applicationPluginInfo_
    Information about the application plugin that was loaded.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ApplicationPluginLoadedEventArgs Class](topic2116.md)   
[ApplicationPluginLoadedEventArgs Members](topic2117.md)

©2024 DriveWorks Ltd. All Rights Reserved.
