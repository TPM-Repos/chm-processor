![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateRuleSearchProcess(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4908.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) > [CreateRuleSearchProcess Method](topic4906.md) : CreateRuleSearchProcess(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_searchString_
    The part of a rule to locate.

Glossary Item Box

Creates a new process capable of searching for parts of a rule in all rules in the project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateRuleSearchProcess( _
       ByVal _searchString_ As String _
    ) As [RuleSearchProcess](topic13212.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim searchString As String
    Dim value As [RuleSearchProcess](topic13212.md)
     
    value = instance.CreateRuleSearchProcess(searchString)  
  
C#|   
---|---  
      
    
    public [RuleSearchProcess](topic13212.md) CreateRuleSearchProcess( 
       string _searchString_
    )  
  
#### Parameters

 _searchString_
    The part of a rule to locate.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)   
[Overload List](topic4906.md)

©2024 DriveWorks Ltd. All Rights Reserved.
