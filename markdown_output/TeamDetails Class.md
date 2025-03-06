TeamDetails Class   
[Members](topic10704.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) : TeamDetails Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about a registered team of users in a DriveWorks group. 

# Object Model

![](dotnetdiagramimages/image539.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public NotInheritable Class TeamDetails   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TeamDetails](topic10703.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public sealed class TeamDetails   
  
# Remarks

Modifications made to an instance of TeamDetails are not immediately reflected in the group from which the instance was obtained. To apply any modifications, call the [DriveWorks.GroupSecurity.TryUpdateTeam](topic3337.md) method.

# Inheritance Hierarchy

System.Object  
**DriveWorks.Security.TeamDetails**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TeamDetails Members](topic10704.md)   
[DriveWorks.Security Namespace](topic10574.md)


