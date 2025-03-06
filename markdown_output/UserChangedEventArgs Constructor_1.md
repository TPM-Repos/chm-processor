       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UserChangedEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [UserChangedEventArgs Class](topic5800.md) : UserChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_user_
    The user that was changed.

Glossary Item Box

Initializes a new instance of the [UserChangedEventArgs](topic5800.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _user_ As [UserDetails](topic10740.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UserChangedEventArgs Class](topic5800.md)   
[UserChangedEventArgs Members](topic5801.md)


