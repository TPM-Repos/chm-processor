![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConnectionEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6936.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ConnectionEventArgs Class](topic6930.md) : ConnectionEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connection_
    The [Connection](topic6909.md) for the event.

Glossary Item Box

Creates a new instance of the [ConnectionEventArgs](topic6930.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _connection_ As [Connection](topic6909.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim connection As [Connection](topic6909.md)
     
    Dim instance As New [ConnectionEventArgs](topic6930.md)(connection)  
  
C#|   
---|---  
      
    
    public ConnectionEventArgs( 
       [Connection](topic6909.md) _connection_
    )  
  
#### Parameters

 _connection_
    The [Connection](topic6909.md) for the event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ConnectionEventArgs Class](topic6930.md)   
[ConnectionEventArgs Members](topic6931.md)

©2024 DriveWorks Ltd. All Rights Reserved.
