       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowHelpTopic Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHelpService Interface](topic315.md) : ShowHelpTopic Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_topicName_
    The full name of the help topic to show.

Glossary Item Box

Shows the help topic with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ShowHelpTopic( _
       ByVal _topicName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHelpService](topic315.md)
    Dim topicName As String
     
    instance.ShowHelpTopic(topicName)  
  
C#|   
---|---  
      
    
    void ShowHelpTopic( 
       string _topicName_
    )  
  
#### Parameters

 _topicName_
    The full name of the help topic to show.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHelpService Interface](topic315.md)   
[IHelpService Members](topic316.md)


