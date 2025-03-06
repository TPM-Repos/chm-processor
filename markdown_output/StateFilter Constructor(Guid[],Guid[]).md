![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateFilter Constructor(Guid[],Guid[])   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1085.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [StateFilter Class](topic1077.md) > [StateFilter Constructor](topic1083.md) : StateFilter Constructor(Guid[],Guid[])  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_includedStates_
    The states in which the filtered entity is included.

_excludedStates_
    The states from which the filtered enttity is excluded.

Glossary Item Box

Initializes a new instance of the [StateFilter](topic1077.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _includedStates_() As Guid, _
       ByVal _excludedStates_() As Guid _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim includedStates() As Guid
    Dim excludedStates() As Guid
     
    Dim instance As New [StateFilter](topic1077.md)(includedStates, excludedStates)  
  
C#|   
---|---  
      
    
    public StateFilter( 
       Guid[] _includedStates_ ,
       Guid[] _excludedStates_
    )  
  
#### Parameters

 _includedStates_
    The states in which the filtered entity is included.
_excludedStates_
    The states from which the filtered enttity is excluded.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StateFilter Class](topic1077.md)   
[StateFilter Members](topic1078.md)   
[Overload List](topic1083.md)

©2024 DriveWorks Ltd. All Rights Reserved.
