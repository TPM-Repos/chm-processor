![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectComponents Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9767.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupOptionsEnvironment Class](topic9759.md) : GetProjectComponents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all components in the source group along with any project specific information and hierarchies. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetProjectComponents() As Task(Of IEnumerable(Of ComponentItemModel))  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupOptionsEnvironment](topic9759.md)
    Dim value As Task(Of IEnumerable(Of ComponentItemModel))
     
    value = instance.GetProjectComponents()  
  
C#|   
---|---  
      
    
    public Task<IEnumerable<ComponentItemModel>> GetProjectComponents()  
  
#### Return Value

A Task that when awaited will return a collection of project component information.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CopyGroupOptionsEnvironment Class](topic9759.md)   
[CopyGroupOptionsEnvironment Members](topic9760.md)

©2024 DriveWorks Ltd. All Rights Reserved.
