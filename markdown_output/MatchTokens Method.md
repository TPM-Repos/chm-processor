![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MatchTokens Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4916.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : MatchTokens Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_collection_
    The collection to search in.

_sequence_
    The sequence to find.

Glossary Item Box

Finds a sequence of RuleTokens within another sequence. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function MatchTokens( _
       ByVal _collection_ As IEnumerable(Of RuleToken), _
       ByVal _sequence_ As IEnumerable(Of RuleToken) _
    ) As IEnumerable(Of Tuple(Of Integer,Integer))  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim collection As IEnumerable(Of RuleToken)
    Dim sequence As IEnumerable(Of RuleToken)
    Dim value As IEnumerable(Of Tuple(Of Integer,Integer))
     
    value = instance.MatchTokens(collection, sequence)  
  
C#|   
---|---  
      
    
    public IEnumerable<Tuple<int,int>> MatchTokens( 
       IEnumerable<RuleToken> _collection_ ,
       IEnumerable<RuleToken> _sequence_
    )  
  
#### Parameters

 _collection_
    The collection to search in.
_sequence_
    The sequence to find.

#### Return Value

A list of all start and end indices of the given sequence.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)

©2024 DriveWorks Ltd. All Rights Reserved.
