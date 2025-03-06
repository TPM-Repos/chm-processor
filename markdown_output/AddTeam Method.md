![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddTeam Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11743.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) : AddTeam Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to add.

Glossary Item Box

Adds the team with the specified identifier to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddTeam( _
       ByVal _teamId_ As Guid _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
    Dim teamId As Guid
     
    instance.AddTeam(teamId)  
  
C#|   
---|---  
      
    
    public void AddTeam( 
       Guid _teamId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to add.

# ![](dotnetimages/collapse.gif)Remarks

If an attempt is made to add a team to an instance which is marked as "All Teams Allowed", i.e. the [IsUniversal](topic11756.md) property returns true, no action is taken by this method until the list is cleared by calling the [Clear](topic11744.md) method first, or until the [IsUniversal](topic11756.md) property is set to false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)

©2024 DriveWorks Ltd. All Rights Reserved.
