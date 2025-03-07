Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MatchTokens Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function MatchTokens( _
       ByVal _collection_ As IEnumerable(Of RuleToken), _
       ByVal _sequence_ As IEnumerable(Of RuleToken) _
    ) As IEnumerable(Of Tuple(Of Integer,Integer))  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


