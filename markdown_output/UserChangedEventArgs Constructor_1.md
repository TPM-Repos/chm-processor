![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UserChangedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5807.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [UserChangedEventArgs Class](topic5800.md) : UserChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_user_
    The user that was changed.

Glossary Item Box

Initializes a new instance of the [UserChangedEventArgs](topic5800.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _user_ As [UserDetails](topic10740.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim user As [UserDetails](topic10740.md)
     
    Dim instance As New [UserChangedEventArgs](topic5800.md)(user)  
  
C#|   
---|---  
      
    
    public UserChangedEventArgs( 
       [UserDetails](topic10740.md) _user_
    )  
  
#### Parameters

 _user_
    The user that was changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[UserChangedEventArgs Class](topic5800.md)   
[UserChangedEventArgs Members](topic5801.md)

©2024 DriveWorks Ltd. All Rights Reserved.
