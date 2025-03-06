![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifySpecificationContextCreated Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2248.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IListenForSpecificationContextCreation Interface](topic2243.md) : NotifySpecificationContextCreated Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The specification context that was created.

Glossary Item Box

Called whenever a specification context is created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifySpecificationContextCreated( _
       ByVal _context_ As [SpecificationContext](topic11149.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IListenForSpecificationContextCreation](topic2243.md)
    Dim context As [SpecificationContext](topic11149.md)
     
    instance.NotifySpecificationContextCreated(context)  
  
C#|   
---|---  
      
    
    void NotifySpecificationContextCreated( 
       [SpecificationContext](topic11149.md) _context_
    )  
  
#### Parameters

 _context_
    The specification context that was created.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IListenForSpecificationContextCreation Interface](topic2243.md)   
[IListenForSpecificationContextCreation Members](topic2244.md)

©2024 DriveWorks Ltd. All Rights Reserved.
