![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Disconnect Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7065.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeNavigationInput Class](topic7058.md) : Disconnect Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connection_
    The connection to remove.

Glossary Item Box

Removes the given connection from this input. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Disconnect( _
       ByVal _connection_ As [Connection](topic6909.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeNavigationInput](topic7058.md)
    Dim connection As [Connection](topic6909.md)
    Dim value As Boolean
     
    value = instance.Disconnect(connection)  
  
C#|   
---|---  
      
    
    public bool Disconnect( 
       [Connection](topic6909.md) _connection_
    )  
  
#### Parameters

 _connection_
    The connection to remove.

#### Return Value

True if the connection was removed, otherwise False.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NodeNavigationInput Class](topic7058.md)   
[NodeNavigationInput Members](topic7059.md)

©2024 DriveWorks Ltd. All Rights Reserved.
