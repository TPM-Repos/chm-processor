Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Indices Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [RuleSearchResult Class](topic13227.md) : Indices Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the array of start and end indices. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Indices As Tuple(Of Integer,Integer)()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleSearchResult](topic13227.md)
    Dim value() As Tuple(Of Integer,Integer)
     
    value = instance.Indices  
  
C#|   
---|---  
      
    
    public Tuple<int,int>[] Indices {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleSearchResult Class](topic13227.md)   
[RuleSearchResult Members](topic13228.md)


