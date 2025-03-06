![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowHelpTopic Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic320.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHelpService Interface](topic315.md) : ShowHelpTopic Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topicName_
    The full name of the help topic to show.

Glossary Item Box

Shows the help topic with the given name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ShowHelpTopic( _
       ByVal _topicName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IHelpService](topic315.md)
    Dim topicName As String
     
    instance.ShowHelpTopic(topicName)  
  
C#|   
---|---  
      
    
    void ShowHelpTopic( 
       string _topicName_
    )  
  
#### Parameters

 _topicName_
    The full name of the help topic to show.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IHelpService Interface](topic315.md)   
[IHelpService Members](topic316.md)

©2024 DriveWorks Ltd. All Rights Reserved.
