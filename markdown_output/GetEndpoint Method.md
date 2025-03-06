![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEndpoint Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12899.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [InputEndpointRef Class](topic12893.md) : GetEndpoint Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project to retrieve the endpoint from.

Glossary Item Box

Gets the endpoint this refers to. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetEndpoint( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [InputConnectionEndpoint](topic7033.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [InputEndpointRef](topic12893.md)
    Dim project As [Project](topic3859.md)
    Dim value As [InputConnectionEndpoint](topic7033.md)
     
    value = instance.GetEndpoint(project)  
  
C#|   
---|---  
      
    
    public abstract [InputConnectionEndpoint](topic7033.md) GetEndpoint( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    The project to retrieve the endpoint from.

#### Return Value

The endpoint this reference refers to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[InputEndpointRef Class](topic12893.md)   
[InputEndpointRef Members](topic12894.md)

©2024 DriveWorks Ltd. All Rights Reserved.
