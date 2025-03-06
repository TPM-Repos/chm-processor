![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseConnectionAdded Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7040.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [InputConnectionEndpoint Class](topic7033.md) : RaiseConnectionAdded Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connection_
    The connection that was added.

Glossary Item Box

Raises the [ConnectionAdded](topic7042.md) event. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseConnectionAdded( _
       ByVal _connection_ As [Connection](topic6909.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [InputConnectionEndpoint](topic7033.md)
    Dim connection As [Connection](topic6909.md)
     
    instance.RaiseConnectionAdded(connection)  
  
C#|   
---|---  
      
    
    protected void RaiseConnectionAdded( 
       [Connection](topic6909.md) _connection_
    )  
  
#### Parameters

 _connection_
    The connection that was added.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[InputConnectionEndpoint Class](topic7033.md)   
[InputConnectionEndpoint Members](topic7034.md)

©2024 DriveWorks Ltd. All Rights Reserved.
