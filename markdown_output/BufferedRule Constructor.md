![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BufferedRule Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6023.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [BufferedRule Class](topic6017.md) : BufferedRule Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceRule_
    The rule which will be buffered.

Glossary Item Box

Initializes a new instance of the [BufferedRule](topic6017.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _sourceRule_ As [IHasRule](topic5947.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim sourceRule As [IHasRule](topic5947.md)
     
    Dim instance As New [BufferedRule](topic6017.md)(sourceRule)  
  
C#|   
---|---  
      
    
    public BufferedRule( 
       [IHasRule](topic5947.md) _sourceRule_
    )  
  
#### Parameters

 _sourceRule_
    The rule which will be buffered.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[BufferedRule Class](topic6017.md)   
[BufferedRule Members](topic6018.md)

©2024 DriveWorks Ltd. All Rights Reserved.
